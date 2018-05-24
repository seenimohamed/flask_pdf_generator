from flask import Flask, render_template, make_response
import pdfkit


app = Flask(__name__)

template_name = 'pdf.html'

# index method to verify the pdf file. Eg. https://localhost:5000
@app.route('/')
def index():
    return render_template(template_name)

# Place holder name method Eg. https://localhost:5000/Seeni
@app.route('/<name>')
def pdf(name) :
    options = {
        'page-size': 'Letter',
        # 'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.5in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'dpi': 500, #to change the pixel size
        'orientation' :'Landscape',
        # 'orientation' :'Potrait',
        'quiet': ''  #to ignore printing the logs in console
    }

    #render a file in flask
    rendered =  render_template(template_name, name=name)

    #set false to not produce result as soon as possible, so that we can make custome response
    pdf = pdfkit.from_string(rendered, False, options=options)

    # custom response section
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'

    # for inline purpose
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    # to make it downloadable uncomment below line
    # response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'

    return response


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
