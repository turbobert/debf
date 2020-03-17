import requests
import sys

def lines_trim_extract(lines, collect_after_first, collect_until_and_without_last, trim_before=None, trim_after=None, trim_start_after=None):
    lines_ = [x.strip() for x in lines if len(x.strip()) > 0 and x.strip() not in trim_before]
    collect_after_first_index = -1
    i=0
    while i < len(lines_)-1:
        if lines_[i] == collect_after_first:
            collect_after_first_index = i+1
            break
        else:
            i+=1
    collect_until_and_without_last_index = -1
    i=0
    while i < len(lines_)-1:
        if lines_[i] == collect_until_and_without_last:
            collect_until_and_without_last_index = i
        i+=1

    result = [ x for x in lines_[collect_after_first_index:collect_until_and_without_last_index] if x not in trim_after ]
    for y in trim_start_after:
        result = [ x for x in result if not x.startswith(y) ]
    return result



if len(sys.argv) == 1:
    print("lookup <FILENAME>       # will retrieve a list of packages and the matching path <PKGNAME> <SPACE> <PATH-WITH-FILENAME>")
    print("url <PKGNAME>           # will retrieve a URL to download the actual package")
    sys.exit(0)

if len(sys.argv) >= 3:

    if sys.argv[1] == "lookup":
        needle = sys.argv[2]
        x = requests.get('https://packages.debian.org/search?searchon=contents&keywords=%s&mode=exactfilename&suite=stable&arch=amd64' % needle)
        lines = lines_trim_extract(x.text.split("\n"), "<table>", "</table>", [], ["<tr>", "</tr>", "<td>", "</td>"], ["<col", "</col", "<th", "<tr"])
        lines = "".join(lines).replace("</a><td", "</a>\n<td").replace(">", "<").split("\n")
        files = []
        for line in lines:
            cols = line.split("<")
            filename = cols[2] + cols[4]
            pkg = cols[9].replace('"', "").split("/")[-1]
            files.append(pkg + " " + filename)
        for line in sorted(files):
            print(line)
    
    if sys.argv[1] == "url":
        needle = sys.argv[2]
        print("Retrieving information from packages.debian.org for package '%s'..." % needle)
        x = requests.get("https://packages.debian.org/%s/%s/%s/download" % ("stable", needle, "amd64"))
        url = [ s for s in x.text.split("\n") if s.find("href=") >= 0 and s.find("ftp.de.debian.org") >= 0 ][0].split('"')[1]
        filename = url.split("/")[-1]
        print("curl '%s' > '%s'     # DOWNLOAD" % (url, filename))
        print("ar -t '%s'      # LIST OUTER CONTAINER" % (filename))
        print("ar -x '%s' data.tar.xz      # EXTRACT data.tar.xz" % (filename))
        print("tar -tJvf data.tar.xz       # LIST CONTENTS data.tar.xz")
