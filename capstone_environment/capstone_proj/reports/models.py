

from django.db import models
from user.models import Profile


"""

# IOCs class with attributes : CVE (Text), URL (Text), Domain  (Text), IP  (Text),
#                              MD5  (Text), SHA1  (Text),  SHA256  (Text), Email  (Text)

"""
class IOCS(models.Model):
    cve = models.TextField(max_length=255, null = True)
    url = models.TextField(max_length=255, null = True)
    domain = models.TextField(max_length=255, null = True)
    ip = models.TextField(max_length=255, null = True)
    md5 = models.TextField(max_length=255, null = True)
    sha1 = models.TextField(max_length=255, null = True)
    sha256 = models.TextField(max_length=255, null = True)
    email = models.TextField(max_length=255, null = True)
    
    """
    # the following function are to brake the IOCs:
    # 
    """
    def cve_br():
        pass
    def url_br():
        pass
    def domain_br():
        pass
    def ip_br():
        pass
    def md5_br():
        pass
    def sha1_br():
        pass
    def sha256_br():
        pass
    def email_br():
        pass




"""

# Report Class with attributes : googleUsersDownloads (list), 
#                                details (text), title (text), reference (url)
#               time(time), Not done
# Relations: one to one with IOCs, and many to one with Profile

"""

class Report(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='profile')
    iocs = models.OneToOneField(IOCS,on_delete= models.DO_NOTHING, null = True, related_name='iocs' )
    reference = models.URLField(max_length=200,null = True)
    details = models.TextField(max_length=255, null = True)
    title = models.CharField(max_length=200,null = True)
    time = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) :
        return f"{self.title}"
   
    
    
    
    


