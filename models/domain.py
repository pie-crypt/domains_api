from db import db

class DomainModel(db.Model):
    __tablename__ = 'domains'
    #id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, primary_key=True)
    creation_date = db.Column(db.String, primary_key=True)
    expiration_date = db.Column(db.String, primary_key=True)
    updated_date = db.Column(db.String, primary_key=True)
    registrar = db.Column(db.String)
    whois_server = db.Column(db.String)
    name_servers = db.Column(db.String)
    status = db.Column(db.String)
    country = db.Column(db.String)
    a = db.Column(db.String)
    aaaa = db.Column(db.String)
    ns = db.Column(db.String)
    cname = db.Column(db.String)
    mx = db.Column(db.String)
    txt = db.Column(db.String)
    soa = db.Column(db.String)
    dnskey = db.Column(db.String)

    def __init__(self, name, creation_date, expiration_date, updated_date, 
                registrar, whois_server, name_servers, status, country, a, 
                aaaa, ns, cname, mx, txt, soa, dnskey):
        self.name = name
        self.creation_date = creation_date
        self.expiration_date = expiration_date
        self.updated_date = updated_date
        self.registrar = registrar
        self.whois_server = whois_server
        self.name_servers = name_servers
        self.status = status
        self.country = country
        self.a = a
        self.aaaa = aaaa
        self.ns = ns
        self.cname = cname
        self.mx = mx
        self.txt = txt
        self.soa = soa
        self.dnskey = dnskey


    def json(self):
        return {"name":self.name, "creation_date":self.creation_date
        , "expiration_date":self.expiration_date, "updated_date":self.updated_date
        , "registrar":self.registrar, "whois_server":self.whois_server
        , "name_servers":self.name_servers, "status":self.status
        , "country":self.country, "A": self.a, "AAAA": self.aaaa
        , "NS": self.ns, "CNAME": self.cname, "MX": self.mx, "TXT": self.txt
        , "SOA": self.soa, "DNSKEY": self.dnskey}

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()