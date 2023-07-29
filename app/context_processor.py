def register_calculated(request):
    mean = 0
    count = 0
    if request.user.is_authenticated:
        if "register" in request.session.keys():
            for key, value in request.session["register"].items():
                if key == "mean":
                    mean = value
                if key == "count":
                    count = value
                
    return {"mean": mean, "count": count}