from pyexpat import model
from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class CategoriesMachines(models.Model):
    codeCategorie=models.TextField(blank=False,primary_key=True)
    nomCategrie = models.TextField(blank=False)

class Atelier(models.Model):
    idAtelier = models.AutoField(primary_key=True)
    nomAtelier = models.TextField(blank=False)

class Machines(models.Model):
    code=models.CharField(max_length=200,primary_key=True)
    type=models.ForeignKey(CategoriesMachines,on_delete=models.CASCADE)
    atelier=models.ForeignKey(Atelier,on_delete=models.CASCADE,null=True)
    brand=models.TextField(blank=False,null=False)
    model=models.TextField(blank=False)
    anneeManifacture=models.DateField()
    currentState=models.TextField(blank=True)
    schudledTime=models.IntegerField()
    timeLosses=models.IntegerField()
    descriptions=models.TextField(blank=True)
    availibilty=models.IntegerField()
    image=models.FileField(default="",upload_to="",null=True,blank=True)

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
    pdg = models.ForeignKey(pdg , on_delete=models.RESTRICT ,null=True, blank=True) 


class utilisateur(models.Model):
    matricule = models.CharField(max_length=20,blank=True,primary_key=True)
    nom = models.CharField(max_length=100,blank=True)
    prenom =models.CharField(max_length=100,blank=True)
    telephone = models.BigIntegerField(blank=True)
    branche = models.ForeignKey(branche, on_delete=models.RESTRICT)
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
    atelier = models.ForeignKey(Atelier,on_delete=models.RESTRICT,null=True,blank=True)

class Intervention(models.Model):
    technicine = models.ForeignKey(technicine,on_delete=models.RESTRICT,null=True)
    machine = models.ForeignKey(Machines,on_delete=models.RESTRICT)
    class Meta():
        abstract=True

class magasin(models.Model):
    article=models.TextField(blank=True)
    quantite=models.PositiveBigIntegerField(blank=True)
    prix=models.FloatField(blank=True)


class sousTraitence(models.Model):
    sousTraitence=models.TextField(blank=True)
    nomRep=models.TextField(blank=True)
    adress =models.TextField(blank=True)
    telephone= models.BigIntegerField(blank=True)
    fax= models.BigIntegerField(blank=True)

class categoriePreventif(models.Model):
    NomAction=models.TextField(blank=True)
    

class IntervenctionCurative(Intervention):
    codeCuratif = models.CharField(max_length=200,primary_key=True)
    dateRapport = models.DateTimeField()
    Sympthomes = ArrayField(models.TextField(blank=True))
    dateDebutAction=models.DateTimeField(blank=True,null=True)
    diagnostique =models.TextField(blank=True,null=True)
    dateFinAction = models.DateTimeField(blank=True,null=True)
    dateCloture = models.DateTimeField(blank=True,null=True)
    TypeDePanne =ArrayField(models.TextField(blank=True))
    etatInterventions = models.TextField(blank=True)
    sousTraitence = models.ForeignKey(sousTraitence,on_delete=models.RESTRICT,null=True,blank=True)

class InterventionPreventive(Intervention):
    codePreventif= models.CharField(max_length=200,primary_key=True)
    date = models.DateField()
    Initials = models.TextField(blank=True)
    planIntervention=models.ForeignKey(categoriePreventif,on_delete=models.RESTRICT)

class cout(models.Model):
    typeDeCout=models.TextField(blank=True)
    cout=models.FloatField(blank=True)
    Curative=models.ForeignKey(IntervenctionCurative,on_delete=models.RESTRICT,null=True,blank=True)
    Prevetive=models.ForeignKey(InterventionPreventive,on_delete=models.RESTRICT,null=True,blank=True)
   
class pieceDeRechange(models.Model):
    nomPiece=models.TextField(blank=True)
    quantite=models.BigIntegerField(blank=True)
    prixTotale=models.FloatField(blank=True)
    detailDePiece=models.ForeignKey(magasin,null=True,on_delete=models.RESTRICT)
    cout=models.ForeignKey(cout,null=True,on_delete=models.RESTRICT)
 
