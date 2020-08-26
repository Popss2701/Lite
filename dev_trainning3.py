import csv
import requests


def data():
    api_key = '759ad65a6f7b965a3d98dd3ff9958e49'
    password = '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'
    shared_secrete = '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'
    shop_name = 'nvphuong1'
    url = 'https://%s:%s@%s.myshopify.com/admin/api/2020-07/customers.json'%(api_key,password,shop_name)
    url += '?fields=id,email,first_name,last_name'
    r = requests.get(url)
    content = r.json()
    with open('customers_file.csv', mode='w')as file:
        fieldnames = ['id', 'email', 'first_name', 'last_name']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in content['customers']:
            writer.writerow(i)

data()
