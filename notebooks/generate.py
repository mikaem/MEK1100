import sys
import re
import nbformat

sage_script = """
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

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

    fb = open('__'+filename, 'w')
    nbformat.write(f, fb)
    fb.close()

def configure_html(filename):
    ff = open(filename).read()
    fl = ff.find('</title>') + 8
    ff = ff[:fl] + sage_script + ff[fl:]
    # Make local figure links fetch from github
    #ff = re.sub('../figs/', 'https://raw.githack.com/mikaem/MEK1100/master/figs/', ff)
    # Rename title
    ff = re.sub('__'+filename[:-12]+' slides', filename[:-12], ff)
    fw = open(filename, 'w')
    fw.write(ff)
    fw.close()

if __name__ == '__main__':
    filename = sys.argv[-1]
    if filename.endswith('ipynb'):
        format_cells(filename)
    elif filename.endswith('html'):
        configure_html(filename)
