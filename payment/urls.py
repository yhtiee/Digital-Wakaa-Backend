from django.urls import path
from .views import *

urlpatterns = [
    path('content_management_mini/create-checkout-session', StripeCheckoutSessionContentMangementMini.as_view()),
    path('content_management_pro/create-checkout-session', StripeCheckoutSessionContentMangementPro.as_view()),
    path('content_management_master/create-checkout-session', StripeCheckoutSessionContentMangementMaster.as_view()),
    path('web_development_pro/create-checkout-session', StripeCheckoutSessionWebDevelopmentPro.as_view()),
    path('web_development_mini/create-checkout-session', StripeCheckoutSessionWebDevelopmentMini.as_view()),
    path('web_development_master/create-checkout-session', StripeCheckoutSessionWebDevelopmentMaster.as_view()),
    path('seo_pro/create-checkout-session', StripeCheckoutSessionSEOPro.as_view()),
    path('seo_mini/create-checkout-session', StripeCheckoutSessionSEOMini.as_view()),
    path('seo_master/create-checkout-session', StripeCheckoutSessionSEOMaster.as_view()),
    path('ppc_pro/create-checkout-session', StripeCheckoutSessionPPCPro.as_view()),
    path('ppc_mini/create-checkout-session', StripeCheckoutSessionPPCMini.as_view()),
    path('ppc_master/create-checkout-session', StripeCheckoutSessionPPCMaster.as_view()),
]
