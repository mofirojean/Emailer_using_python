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
    def __init__(self, companyName):
        self.companyName = companyName

    # Generates the pdf document and saves it, in the Docs folder
    def generateTemplate(self, userName):
        """ Generates a Word document from the template file"""
        doc = DocxTemplate("./Template/Template.docx")
        context = {'company': self.companyName, 'name': userName}
        doc.render(context)
        fileName = f"./Docs/{userName}.docx"
        doc.save(fileName)

        # converts to pdf
        output = convert(source=fileName, output_dir="./Docs", soft=1)

        # Deletes the word documented generated from the template
        file = pathlib.Path(fileName)
        file.unlink()

        # Returns the path of the pdf file generated
        return output
