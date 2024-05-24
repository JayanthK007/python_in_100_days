import requests
import datetime
import dotenv
import os

dotenv.load_dotenv()

user_params={
    'token':os.getenv('TOKEN'),
    'username':os.getenv('USER'),
    'agreeTermsOfService':"yes",
    'notMinor':"yes"
}
# response=requests.post(url='https://pixe.la/v1/users',json=user_params)

graph_params={
    'id':'learning',
    'name':'track-my-habit',
    'unit':'hours',
    'type':'int',
    "color":"shibafu"
}
# graph_response=requests.post(url=f'https://pixe.la/v1/users/{os.getenv('USER')}/graphs',headers={'X-USER-TOKEN':os.getenv('TOKEN')},json=graph_params)
pixel_params={
    'date':datetime.date.today().strftime(format='%Y%m%d'),
    'quantity':'2'
}
# pixel_response=requests.post(url=f' https://pixe.la/v1/users/{os.getenv('USER')}/graphs/learning',headers={'X-USER-TOKEN':os.getenv('TOKEN')},json=pixel_params)

# pixel_update_resp=requests.put(url=f'https://pixe.la/v1/users/{os.getenv('USER')}/graphs/learning/{datetime.date.today().strftime(format='%Y%m%d')}',headers={'X-USER-TOKEN':os.getenv('TOKEN')},json={
#     'quantity':'10'
# })

pixel_delete_resp=requests.delete(url=f'https://pixe.la/v1/users/{os.getenv('USER')}/graphs/learning/{datetime.date.today().strftime(format='%Y%m%d')}',headers={'X-USER-TOKEN':os.getenv('TOKEN')})

print(pixel_delete_resp.text)