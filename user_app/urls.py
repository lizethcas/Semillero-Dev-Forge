from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.documentation import include_docs_urls
from .views import (
    UserAgentSignupView, 
    UserSigninView, 
    UserAgentSignoutView,
    UserCustomerInitialSignupView,
    UserCustomerCompleteSignupView,
    UserCustomerSignoutView,
    CheckSessionView,
    ConsultUserCustomerById,
    oauth2_callback,
    start_auth_flow,
    UserCustomerOAuth2SignupView,
    VerifyEmailView,
)

urlpatterns = [
    path('api/signup_agent/', UserAgentSignupView.as_view(), name='signup_agent'),
    path('api/signout_agent/', UserAgentSignoutView.as_view(), name='signout_agent'),

    path('api/signup_customer_initial/', UserCustomerInitialSignupView.as_view(), name='signup_customer_initial'),
    path('api/signup_customer_complete/', UserCustomerCompleteSignupView.as_view(), name='signup_customer_complete'),

    path('api/signout_customer/', UserCustomerSignoutView.as_view(), name='signout_customer'),

    path('api/signin/', UserSigninView.as_view(), name='signin'),

    path('api/consult_customer/<int:id>/', ConsultUserCustomerById.as_view(), name='consult_customer'),

    path('docs/', include_docs_urls(title='API Documentation')),

    path('api/check_session/', CheckSessionView.as_view(), name='check_session'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('oauth2callback/', oauth2_callback, name='oauth2callback'),
    path('start-auth/', start_auth_flow, name='start_auth_flow'),

    path('api/signup_customer_oauth2/', UserCustomerOAuth2SignupView.as_view(), name='signup_customer_oauth2'),
    path('api/verify_email/', VerifyEmailView.as_view(), name='verify_email'),
]
