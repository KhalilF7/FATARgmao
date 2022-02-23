from django.db import models

# Create your models here.
class branche(models.Model):
    code = models.CharField(max_length=200,primary_key=True)
    nom = models.TextField(null=True,blank=True)
    adress = models.TextField(blank=True)
    pays = models.TextField(blank=True)
    email = models.TextField(blank=True)
    telephone = models.BigIntegerField(blank=True)
    fax = models.BigIntegerField(blank=True)

class contract(models.Model):
    contractID = models.CharField(max_length=100,primary_key=True)
    contactType = models.TextField(null=True)
    dateDebut = models.DateField(null=True)
    dateFin = models.DateField(null=True)
    contactFile = models.TextField(null=True)
    

class utilisateur(models.Model):
    matricule = models.CharField(max_length=20,blank=True)
    cin = models.BigIntegerField(primary_key=True,default=0)
    nom = models.CharField(max_length=100,blank=True)
    prenom =models.CharField(max_length=100,blank=True)
    dateNaissance = models.DateField(blank=True)
    email = models.EmailField(blank=True)
    telephone = models.BigIntegerField(blank=True)
    etatCivile = models.CharField(max_length=50,blank=True)
    branche = models.ForeignKey(branche, on_delete=models.CASCADE)
    contract = models.OneToOneField(contract,on_delete=models.CASCADE,null=True,blank=True)
    # fucntion to not add the table into the db , but creat child with the father attr
    class Meta():
        abstract=True
 
class responsable(utilisateur): 
    username = models.CharField(max_length=500)
    password= models.TextField(blank=True)
    
class technicine(utilisateur):
    username = models.CharField(max_length=200)
    password = models.TextField(blank=True)

class diplome(models.Model):
    diplomeID = models.CharField(max_length=200,primary_key=True)
    titreDiplome = models.TextField(null=True)
    fileDiplome =models.TextField(null=True)
    technicine = models.ForeignKey(technicine,on_delete=models.CASCADE)

    
class formation(models.Model):
    formationID = models.CharField(max_length=200,primary_key=True)
    titreformation = models.TextField(null=True)
    fileFormation =models.TextField(null=True)
    technicine = models.ForeignKey(technicine,on_delete=models.CASCADE)

