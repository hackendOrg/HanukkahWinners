def print_to_html(score_board, html_path):
    html_content = "<!DOCTYPE html>\n" + \
                   "<html>\n" + \
                   "<head>\n" + \
                   "<style>\n" + \
                   "table,th,td {\n" + \
                   "border: 2px solid black;\n" + \
                   "border-collapse: collapse;\n" + \
                   "}\n" + \
                   "th, td {\n" + \
                   "padding: 5px;\n" + \
                   "text-align: left;\n" + \
                   "}\n" + \
                   "</style>\n" + \
                   "</head>\n" + \
                   "<body style=\"font-family:Comic Sans MS;\"\n>" + \
                   "<div align=\"center\"><font size=\"6\" color = \"red\"> Hackend's Hanukkah Games 2018 " \
                   "</font></div>\n" + \
                   "<br>\n" + \
                   "<table style=\"width:75%;\" align=\"center\" bgcolor=\"#FFFFCC\">\n" + \
                   "<tr>\n" + \
                   "<th>Name</th>\n" + \
                   "<th>Score</th>\n" + \
                   "</tr>\n"
    for pair in score_board:
        html_content += "<tr><td>" + pair[0] + "</td><td>" + str(pair[1]) + "</td></tr>"
    html_content += "</table>\n" + \
                    "</body>\n" + \
                    "</html>\n"
    with open(html_path, 'wb') as f:
        f.write(html_content.encode('UTF-8'))

