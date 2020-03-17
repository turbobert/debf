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

needle = sys.argv[1]
x = requests.get('https://packages.debian.org/search?searchon=contents&keywords=%s&mode=exactfilename&suite=stable&arch=amd64' % needle)
#print(x.text)

lines = lines_trim_extract(x.text.split("\n"), "<table>", "</table>", [], ["<tr>", "</tr>", "<td>", "</td>"], ["<col", "</col", "<th", "<tr"])
lines = "".join(lines).replace("</a><td", "</a>\n<td").replace(">", "<").split("\n")

files = []

for line in lines:
    cols = line.split("<")
    filename = cols[2] + cols[4]
    pkg = cols[9].replace('"', "").split("/")[-1]
    #print("filename='%s'" % filename)
    #print("package='%s'" % pkg)
    files.append(pkg + " " + filename)

for line in sorted(files):
    print(line)
