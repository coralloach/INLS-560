# For Assignment 06, I have marked the comments for grading with an * (e.g. #*)


import os #* Provides functions for interacting with the operating system
import re #* Regular Expression Operations compare pre-defined regular expressions
# to code, searching for matching patterns and expressions

# Slugify function.
def slugify(title):
    """Convert the page title to a filename-friendly slug."""
    #* Here is an example of an if statement
    if title.lower() == "home":  # Ensure 'Home' becomes 'index.html'
        return "index.html"
    return re.sub(r'\W+', '-', title.strip().lower()) + ".html"

# Navigation Function.
def generate_nav(titles, active_title):
    """Generate a dynamic navigation bar with an active page highlight."""
    nav_links = ""
    #* Here is an example of a for loop
    for title in titles:
        filename = slugify(title)
        active_class = ' class="active"' if title == active_title else ""
        nav_links += f'\t\t\t<a href="{filename}"{active_class}>{title}</a>\n'
    return nav_links.strip()

# Create HTML Function.
def create_html_file(title, titles, output_dir="build"):
    """Generate and write HTML content based on the page title."""
    filename = slugify(title)
    nav = generate_nav(titles, active_title=title)
    #* Here is an example of an f-string
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <nav>
            {nav}
        </nav>
        <div class="content">
            <h1>{title}</h1>
            <p>This is the {title.lower()} content.</p>
        </div>
    </body>
    </html>
    """

    output_path = os.path.join(output_dir, filename)
   #* Here is where the directory is created.
    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

    with open(output_path, 'w') as file:
        #* Here is an example of file.write
        file.write(html_content)

    print(f"Created {filename} in the '{output_dir}' directory.")

# Create CSS file function.
#* This is where the pass statement was. I have marked up the wrong file, but
# in the original web_build.py file, the pass statement was directly under
# def create_css_file():, to indicate that there would be code here later
def create_css_file(output_dir="build"):
    """Generate and write the style.css file based on a dictionary of styles."""
    #* Here is an example of a dictionary
    styles = {
        "font-family": "Calibri",             # font family
        "body-background": "#7BAFD4",     # Background color for .content
        "nav-background": "#13294B",          # Background color for nav
        "nav-a-color": "#4B9CD3",              # Text color for nav links
        "nav-a-active-color": "#ffffff"
    }

    css_content = f"""
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: {styles["font-family"]};
    }}

    body {{
        background-color: {styles["body-background"]};
    }}

    nav {{
        background-color: {styles["nav-background"]};
        padding: 10px;
    }}

    nav a {{
        color: {styles["nav-a-color"]};
        margin-right: 10px;
        text-decoration: none;
    }}

    nav a.active {{
        color: {styles["nav-a-active-color"]};
        font-weight: bold;
    }}

    .content {{
        background-color: #F8F8F8;
        padding: 20px;
        margin: 20px;
    }}
    """

    css_path = os.path.join(output_dir, "style.css")
    #* Here is an example of with open() as file
    with open(css_path, 'w') as file:
        file.write(css_content)

    print(f"Created style.css in the '{output_dir}' directory.")

# Main function.
def main():
    """Main function to generate pages and styles. MUST HAVE HOME!!!"""
    titles = ["Home", "About Me", "Store", "Contact Us"]

    # Create HTML files for each title
    #* Here is an example of a method, the create_html_file()
    for title in titles:
        create_html_file(title, titles)

    # Create the style.css file (previously commented out).
        create_css_file() 

if __name__ == "__main__":
    main()