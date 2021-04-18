from .views import (
    PoliceComplaintViewSet,
    PoliceComplaintUpdateViewSet,
    GenderViewSet,
    AllegationViewSet,
    EthnicityViewSet,
    FadoViewSet,
    PrecinctViewSet,
    ContactReasonViewSet,
    OutcomeDescriptionReasonViewSet,
    BoardDispositionViewSet
)
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("police-complaints", PoliceComplaintViewSet, "police-complaints")
router.register("police-complaints-update", PoliceComplaintUpdateViewSet, "police-complaints-update")
router.register("gender", GenderViewSet, "gender")
router.register("allegation", AllegationViewSet, "allegation")
router.register("ethnicity", EthnicityViewSet, "ethnicity")
router.register("fado", FadoViewSet, "fado")
router.register("precinct", PrecinctViewSet, "precinct")
router.register("contact-reason", ContactReasonViewSet, "contact-reason")
router.register("outcome-description", OutcomeDescriptionReasonViewSet, "outcome-description")
router.register("board-disposition", BoardDispositionViewSet, "board-disposition")



urlpatterns = router.urls