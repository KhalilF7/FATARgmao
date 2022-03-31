from django.db import models

# Create your models here.
class Atelier(models.Model):
    idAtelier = models.AutoField(primary_key=True)
    nomAtelier = models.TextField(blank=False)

class pdg(models.Model):
    nom = models.CharField(max_length=200,blank=True)
    prenom = models.CharField(max_length=200,blank=True)  
    login = models.CharField(max_length=200,blank=True)
    motDePasse = models.CharField(max_length=200,blank=True)  
class branche(models.Model):
    code = models.CharField(max_length=200,primary_key=True)
    nom = models.TextField(null=True,blank=True)
    adress = models.TextField(blank=True)
    pays = models.TextField(blank=True)
    email = models.TextField(blank=True)
    telephone = models.BigIntegerField(blank=True)
    fax = models.BigIntegerField(blank=True)
    pdg = models.ForeignKey(pdg , on_delete=models.CASCADE ,null=True, blank=True) 

class utilisateur(models.Model):
    matricule = models.CharField(max_length=20,blank=True,primary_key=True)
    nom = models.CharField(max_length=100,blank=True)
    prenom =models.CharField(max_length=100,blank=True)
    telephone = models.BigIntegerField(blank=True)
    branche = models.ForeignKey(branche, on_delete=models.CASCADE)
    # fucntion to not add the table into the db , but creat child with the father attr
    class Meta():
        abstract=True
 
class responsable(utilisateur): 
    login = models.CharField(max_length=500,blank=True)
    motDePasse= models.TextField(blank=True)
    
class technicine(utilisateur):
    login = models.CharField(max_length=200,blank=True)
    motDePasse = models.TextField(blank=True)
    suppheurePrice = models.IntegerField(null=True,blank=True)
    isResponsableMaintenance = models.BooleanField(default=False)
    isResponsableProduction = models.BooleanField(default=False)
    atelier = models.ForeignKey(Atelier,on_delete=models.CASCADE,null=True,blank=True)
