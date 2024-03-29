from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client,get_tracker_conf
from django.conf import settings

class FDFSStorage(Storage):
    '''fast dfs文件存储类'''
    def __init__(self, client_conf=None, base_url=None):
        if client_conf == None:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf

        if base_url == None:
            base_url = settings.FDFS_STORAGE_URL
        self.base_url = base_url

    def _open(self,name,mode='rb'):
        '''打开文件时使用'''
        pass

    def _save(self,name,content):
        '''保存文件时使用'''

        #create fdfs client object
        trackers = get_tracker_conf(self.client_conf)
        client = Fdfs_client(trackers)

        #upload file to fdfs system
        res = client.upload_by_buffer(content.read())
        # dict
        # {
        #     'Group name': group_name,
        #     'Remote file_id': remote_file_id,
        #     'Status': 'Upload successed.',
        #     'Local file name': '',
        #     'Uploaded size': upload_size,
        #     'Storage IP': storage_ip
        # }
        if res.get('Status') != 'Upload successed.':
            # upload failed
            raise Exception('上传文件到fast dfs失败')

        # 获取返回到文件ID
        filename = res.get('Remote file_id')

        return filename.decode()

    def exists(self, name):
        '''Django判断文件名是否有效'''
        return False

    def url(self, name):
        '''返回 访问文件name 所需的url路径'''
        # django调用url方法时，所传递的 name参数：数据库 表中所存的 文件名字符串(即是，fastdfs中存储文件时 使用的文件名)
        return self.base_url + name

