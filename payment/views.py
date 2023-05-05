from django.conf import settings
import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect

stripe.api_key = settings.STRIPE_SECRET_KEY

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
