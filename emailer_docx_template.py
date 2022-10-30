"""
 ***********************************************
 Generates a pdf document from the template file
 ***********************************************
"""
import pathlib
from msoffice2pdf import convert
from docxtpl import DocxTemplate


class GenerateTemplate:
    """Initialize parameters"""
    def __init__(self, company_name):
        self.companyName = company_name

    # Generates the pdf document and saves it, in the Docs folder
    def generate_template(self, user_name):
        """ Generates a Word document from the template file"""
        doc = DocxTemplate("./Template/Template.docx")
        context = {'company': self.companyName, 'name': user_name}
        doc.render(context)
        file_name = f"./Docs/{user_name}.docx"
        doc.save(file_name)

        # converts to pdf
        output = convert(source=file_name, output_dir="./Docs", soft=1)

        # Deletes the word documented generated from the template
        file = pathlib.Path(file_name)
        file.unlink()

        # Returns the path of the pdf file generated
        return output
