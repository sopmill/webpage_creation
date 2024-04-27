from xml.etree import ElementTree as ET

def indent(elem, level=0):
    """
    Add indentation to XML/HTML element.
    """
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def txt_to_html(txt_file, html_file):
    """
    Converts a text file with headers and paragraphs to an HTML file.
    This script is for multiple news articles.

    Args:
        txt_file (str): Path to the text file containing articles and headers.
        html_file (str): Path to the output HTML file.
    """
    # Read text file content
    with open(txt_file, 'r') as f:
        content = f.readlines()

    # Create root element for HTML
    root = ET.Element("html")

    # Create head and body elements
    head = ET.SubElement(root, "head")
    title = ET.SubElement(head, "title")
    title.text = "My News Aggregation Site"
    body = ET.SubElement(root, "body")

    # Loop through articles and headers
    for i in range(0, len(content), 2):
        header = content[i].strip()
        paragraph = content[i+1].strip()

        # Create header element for each article
        h1 = ET.SubElement(body, "h1")
        h1.text = header
        
        # Create paragraph element as sibling of header
        p = ET.Element("p")
        p.text = paragraph
        body.append(p)
        

    # Indent the XML tree
    indent(root)


    # Write HTML tree to file
    with open(html_file, 'wb') as f:
        tree = ET.ElementTree(root)
        tree.write(f, encoding='utf-8')

txt_file = "my_text.txt"
html_file = "all_news_articles.html"
txt_to_html(txt_file, html_file)

print(f"Converted text file '{txt_file}' to HTML file '{html_file}'.")
