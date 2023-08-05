# import markdown

# def convert_markdown_to_html(markdown_file, html_file):
#     with open(markdown_file, 'r') as f:
#         markdown_content = f.read()

#     html_content = markdown.markdown(markdown_content)

#     with open(html_file, 'w') as f:
#         f.write(html_content)

# # Usage example:
# convert_markdown_to_html('html.markdown', 'output.html')


import markdown

def generate_table_of_contents(md_file):
    with open(md_file, 'r') as file:
        markdown_content = file.read()

    # Parse the Markdown content
    md = markdown.Markdown(extensions=['markdown.extensions.toc'])

    # Convert Markdown to HTML
    html_content = md.convert(markdown_content)

    # Retrieve the generated table of contents
    table_of_contents = md.toc

    # Print the table of contents
    print(table_of_contents)

    # Save the modified content with clickable table of contents
    with open('output.html', 'w') as file:
        file.write(html_content)

# Provide the path to your Markdown file
markdown_file = 'html.markdown'

# Generate and display the table of contents
generate_table_of_contents(markdown_file)
