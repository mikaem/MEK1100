import sys
import nbformat

sage_script = """
<script src="https://sagecell.sagemath.org/static/embedded_sagecell.js"></script>
<script>$(function () {
    // Make *any* div with class 'sagecell-sage' an executable Sage cell
    // Their results will be linked, only within language type
    sagecell.makeSagecell({inputLocation: 'div.sagecell-sage',
                           linked: true,
                           languages: ['sage'],
                           evalButtonText: 'Evaluate'});
});
</script>
"""

def format_cells(filename):
    f = nbformat.read(filename, nbformat.NO_CONVERT)
    for cell in f['cells']:
        if cell['cell_type'] == 'code':
            if hasattr(cell['metadata'], 'tags'):
                if 'sage' in cell['metadata']['tags']:
                    source = cell['source']
                    newsource = """<div class='sagecell-sage'><script type='text/x-sage'>
%s
</script></div>"""%(source)
                    cell['source'] = newsource
                    cell['cell_type'] = 'markdown'
                    del cell['execution_count']
                    del cell['outputs']

    fb = open(filename[:-6]+'_sage.ipynb', 'w')
    nbformat.write(f, fb)
    fb.close()

def add_sagescript(filename):
    ff = open(filename).read()
    fl = ff.find('</title>') + 8
    ff = ff[:fl] + sage_script + ff[fl:]
    fw = open(filename, 'w')
    fw.write(ff)
    fw.close()

if __name__ == '__main__':
    filename = sys.argv[-1]
    if filename.endswith('ipynb'):
        format_cells(filename)
    elif filename.endswith('html'):
        add_sagescript(filename)
