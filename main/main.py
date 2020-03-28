import dns
from sqlalchemy.orm import Session

import config.convert_long_url_to_domain
import config.database
import config.dns_lookup
from model.cname import Cname
from model.http_requests import HttpRequests

if __name__ == '__main__':
    master_session: Session = config.database.connect_master_session()
    replica_session: Session = config.database.connect_replica_session()

    result = replica_session.query(HttpRequests).all()

    replica_session.close()

    http_request: HttpRequests
    for http_request in result:
        domain = config.convert_long_url_to_domain.convert_long_url_to_domain(http_request.url)
        # domain = 'f7ds.liberation.fr'
        list_cname = config.dns_lookup.dns_lookup(domain)

        if len(list_cname) > 0:
            for cname in list_cname:
                new_cname_obj = Cname(http_requests_id=http_request.id,
                                      cname=cname['cname'],
                                      ip=cname['ip'])
                master_session.add(new_cname_obj)
            master_session.commit()

    master_session.close()