from django.db import models

# Create your models here.

class pdg(models.Model):
    nom = models.CharField(max_length=200,blank=True)
    prenom = models.CharField(max_length=200,blank=True)  
    login = models.CharField(max_length=200,blank=True)
    password = models.CharField(max_length=200,blank=True)  
class branche(models.Model):
    code = models.CharField(max_length=200,primary_key=True)
    nom = models.TextField(null=True,blank=True)
    adress = models.TextField(blank=True)
    pays = models.TextField(blank=True)
    email = models.TextField(blank=True)
    telephone = models.BigIntegerField(blank=True)
    fax = models.BigIntegerField(blank=True)
    pdg = models.ForeignKey(pdg , on_delete=models.CASCADE ,null=True, blank=True)
class contract(models.Model):
    contractID = models.CharField(max_length=100,primary_key=True)
    contactType = models.TextField(null=True)
    dateDebut = models.DateField(null=True)
    dateFin = models.DateField(null=True)
    contact = models.FileField(null=True)    

class utilisateur(models.Model):
    matricule = models.CharField(max_length=20,blank=True)
    cin = models.CharField(primary_key=True,max_length=50)
    nom = models.CharField(max_length=100,blank=True)
    prenom =models.CharField(max_length=100,blank=True)
    dateNaissance = models.DateField(blank=True)
    email = models.EmailField(blank=True)
    telephone = models.BigIntegerField(blank=True)
    etatCivile = models.CharField(max_length=50,blank=True)
    branche = models.ForeignKey(branche, on_delete=models.CASCADE)
    isDeleted=models.BooleanField(default=False)
    # fucntion to not add the table into the db , but creat child with the father attr
    class Meta():
        abstract=True
 
class responsable(utilisateur): 
    username = models.CharField(max_length=500,blank=True)
    password= models.TextField(blank=True)
    
class technicine(utilisateur):
    username = models.CharField(max_length=200,blank=True)
    password = models.TextField(blank=True)
    suppheurePrice = models.IntegerField(null=True,blank=True)
    isResponsableMaintenance = models.BooleanField(default=False)
    isResponsableProduction = models.BooleanField(default=False)
