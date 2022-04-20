def kuulujutt(hetke_teadjate_arv, korrutatav_arv, tundide_arv_) :
    if tundide_arv_ == 0 :
        print(hetke_teadjate_arv)
    else:
        hetke_teadjate_arv = (hetke_teadjate_arv * korrutatav_arv) + hetke_teadjate_arv
        #print(hetke_teadjate_arv)
        return kuulujutt(hetke_teadjate_arv, korrutatav_arv, tundide_arv_ - 1)

kuulujutt(3, 3, 10)