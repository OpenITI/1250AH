
import re

EMPTY = "# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."
EMPTY = "\n+#(?: \.){10,} *\n*"
fp = "1230IbnAhmadDasuqi.HashiyaCalaMukhtasarMacani.Sham19Y0147062-ara1"

fp1 = "0792IbnCumarTaftazani.MukhtasarMacani.Sham19Y0147062BK1-ara1"
fp2 = "1230IbnAhmadDasuqi.HashiyaCalaMukhtasarMacani.Sham19Y0147062BK2-ara1"


with open(fp, mode="r", encoding="utf-8") as file:
    text = file.read()
splitter = "#META#Header#End#\n"
header, text = text.split(splitter)

page_content = ""
page_no = ""
info = "\n\n#META# Note: This text file originally contained two separate works: 0792IbnCumarTaftazani.MukhtasarMacani and 1230IbnAhmadDasuqi.HashiyaCalaMukhtasarMacani. """
info_1 = info + "This text file contains only the first work: 0792IbnCumarTaftazani.MukhtasarMacani\n\n"
info_2 = info + "This text file contains only the second work: 1230IbnAhmadDasuqi.HashiyaCalaMukhtasarMacani\n\n"
text_1 = header + info_1 + splitter
text_2 = header + info_2 + splitter
for page in re.split(r"(PageV[^P]+P\d+)", text):
    if page.startswith("Page"):
        page_no = page
        try:
            part_1, part_2 = re.split(r"\n+# ===+ *\n+", page_content)
        except:
            print("PAGE CAN'T BE SPLIT:")
            print(page_content)
            print(page_no)
            print("----")
        part_1 = re.sub(EMPTY, "", part_1)
        if part_1.strip():
            text_1 += f"{part_1}\n{page_no}\n"
        part_2 = re.sub(EMPTY, "", part_2)
        if part_2.strip():
            text_2 += f"{part_1}\n{page_no}\n"
        page_content = None
        page_no = None
    else:
        page_content = page

# clean up:
#text_1 = re.sub(r" +\.\.\. *\n+(PageV[^P]+P\d+)\n+# ", r" \1 ", text_1)
#text_2 = re.sub(r" +\.\.\. *\n+(PageV[^P]+P\d+)\n+# ", r" \1 ", text_2)

with open(fp1, mode="w", encoding="utf-8") as file:
    file.write(text_1)
with open(fp2, mode="w", encoding="utf-8") as file:
    file.write(text_2)
    
