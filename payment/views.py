from django.conf import settings
import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

stripe.api_key = settings.STRIPE_SECRET_KEY

@method_decorator(csrf_exempt, name='dispatch')
class StripeCheckoutSessionContentMangementMini(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'CONTENT MANAGEMENT MINI PLAN',
                            },
                            'unit_amount': 10000,
                        },
                        'quantity': 1,
                    }
                ],
                payment_method_types = ["card"],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        
        except:
            return Response(data={
                "error": "something went wrong creating stripe checkout session",
            }, status=status.HTTP_400_BAD_REQUEST)
        
@method_decorator(csrf_exempt, name='dispatch')
class StripeCheckoutSessionContentMangementPro(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'CONTENT MANAGEMENT PRO PLAN',
                            },
                            'unit_amount': 20000,
                        },
                        'quantity': 1,
                    }
                ],
                payment_method_types = ["card"],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        
        except:
            return Response(data={
                "error": "something went wrong creating stripe checkout session",
            }, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class StripeCheckoutSessionContentMangementMaster(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'CONTENT MANAGEMENT MASTER PLAN',
                            },
                            'unit_amount': 40000,
                        },
                        'quantity': 1,
                    }
                ],
                payment_method_types = ["card"],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        
        except:
            return Response(data={
                "error": "something went wrong creating stripe checkout session",
            }, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class StripeCheckoutSessionWebDevelopmentMini(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'WEB DEVELOPMENT MINI PLAN',
                            },
                            'unit_amount': 10000,
                        },
                        'quantity': 1,
                    }
                ],
                payment_method_types = ["card"],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        
        except:
            return Response(data={
                "error": "something went wrong creating stripe checkout session",
            }, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class StripeCheckoutSessionWebDevelopmentPro(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'WEB DEVELOPMENT PRO PLAN',
                            },
                            'unit_amount': 20000,
                        },
                        'quantity': 1,
                    }
                ],
                payment_method_types = ["card"],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        
        except:
            return Response(data={
                "error": "something went wrong creating stripe checkout session",
            }, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class StripeCheckoutSessionWebDevelopmentMaster(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'WEB DEVELOPMENT MASTER PLAN',
                            },
                            'unit_amount': 40000,
                        },
                        'quantity': 1,
                    }
                ],
                payment_method_types = ["card"],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        
        except:
            return Response(data={
                "error": "something went wrong creating stripe checkout session",
            }, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class StripeCheckoutSessionSEOMini(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'SEO MINI PLAN',
                            },
                            'unit_amount': 10000,
                        },
                        'quantity': 1,
                    }
                ],
                payment_method_types = ["card"],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        
        except:
            return Response(data={
                "error": "something went wrong creating stripe checkout session",
            }, status=status.HTTP_400_BAD_REQUEST)
        
@method_decorator(csrf_exempt, name='dispatch')
class StripeCheckoutSessionSEOPro(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'SEO PRO PLAN',
                            },
                            'unit_amount': 20000,
                        },
                        'quantity': 1,
                    }
                ],
                payment_method_types = ["card"],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        
        except:
            return Response(data={
                "error": "something went wrong creating stripe checkout session",
            }, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class StripeCheckoutSessionSEOMaster(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'SEO MASTER PLAN',
                            },
                            'unit_amount': 40000,
                        },
                        'quantity': 1,
                    }
                ],
                payment_method_types = ["card"],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        
        except:
            return Response(data={
                "error": "something went wrong creating stripe checkout session",
            }, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class StripeCheckoutSessionPPCMini(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'PPC MINI PLAN',
                            },
                            'unit_amount': 10000,
                        },
                        'quantity': 1,
                    }
                ],
                payment_method_types = ["card"],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        
        except:
            return Response(data={
                "error": "something went wrong creating stripe checkout session",
            }, status=status.HTTP_400_BAD_REQUEST)
        
@method_decorator(csrf_exempt, name='dispatch')       
class StripeCheckoutSessionPPCPro(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'PPC Pro PLAN',
                            },
                            'unit_amount': 20000,
                        },
                        'quantity': 1,
                    }
                ],
                payment_method_types = ["card"],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        
        except:
            return Response(data={
                "error": "something went wrong creating stripe checkout session",
            }, status=status.HTTP_400_BAD_REQUEST)
        
@method_decorator(csrf_exempt, name='dispatch')       
class StripeCheckoutSessionPPCMaster(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'PPC MASTER PLAN',
                            },
                            'unit_amount': 40000,
                        },
                        'quantity': 1,
                    }
                ],
                payment_method_types = ["card"],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        
        except:
            return Response(data={
                "error": "something went wrong creating stripe checkout session",
            }, status=status.HTTP_400_BAD_REQUEST)
