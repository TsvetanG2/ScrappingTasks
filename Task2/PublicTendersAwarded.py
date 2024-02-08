import xml.etree.ElementTree as ET
import pandas as pd

def scrape_xml(file_path):
    data_list = []
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        notices = root.findall('.//FullNotice/Notice')
        awards = root.findall('.//Awards/AwardDetail')
        links = root.findall('.//AdditionalDetails/AdditionalDetail')

        for notice, award, link in zip(notices, awards, links):
            data_dict = {}

            data_dict["Publish date"] = notice.find('PublishedDate').text if notice.find('PublishedDate') is not None else None
            data_dict["Date of award"] = award.find('AwardedDate').text if award.find(
                'AwardedDate') is not None else None
            data_dict["Title"] = notice.find('Title').text if notice.find('Title') is not None else None
            data_dict["Short description"] = notice.find('CpvDescription').text if notice.find('CpvDescription') is not None else None
            data_dict["Awarded company"] = award.find('SupplierName').text if award.find('SupplierName') is not None else None
            data_dict["Awarded company address"] = award.find('SupplierAddress').text if award.find(
                'SupplierAddress') is not None else None
            data_dict["Awarded value"] = notice.find('Status').text if notice.find('Status') is not None else None
            data_dict["url"] = link.find('Link').text if link.find('Link') is not None else "N/A"

            data_list.append(data_dict)

        return data_list

    except FileNotFoundError:
        print("Error")


file_path = "notices.xml"
final_notice = scrape_xml(file_path)
for notice in final_notice:
    print(notice)

df = pd.DataFrame(final_notice, columns=["Publish date", "Date of award", "Title", "Short description", "Awarded company", "Awarded value", "Awarded company address", "url"])
final_notice_path = 'final_notice.xlsx'
df.to_excel(final_notice_path, index=False)
print(f"Excel file '{final_notice_path}' has been created.")