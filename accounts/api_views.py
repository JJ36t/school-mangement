from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserRegistrationSerializer

User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
    """
    API endpoint for user login
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({
            'error': 'اسم المستخدم وكلمة المرور مطلوبان'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': UserSerializer(user).data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'الحساب غير نشط'
            }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            'error': 'بيانات الدخول غير صحيحة'
        }, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_api(request):
    """
    API endpoint for user registration
    """
    serializer = UserRegistrationSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_api(request):
    """
    API endpoint to get user profile
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile_api(request):
    """
    API endpoint to update user profile
    """
    serializer = UserSerializer(request.user, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password_api(request):
    """
    API endpoint to change user password
    """
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')
    
    if not old_password or not new_password:
        return Response({
            'error': 'كلمة المرور الحالية والجديدة مطلوبتان'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if not request.user.check_password(old_password):
        return Response({
            'error': 'كلمة المرور الحالية غير صحيحة'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.set_password(new_password)
    request.user.save()
    
    return Response({
        'message': 'تم تغيير كلمة المرور بنجاح'
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_api(request):
    """
    API endpoint for user logout
    """
    try:
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
        return Response({
            'message': 'تم تسجيل الخروج بنجاح'
        })
    except Exception as e:
        return Response({
            'error': 'حدث خطأ أثناء تسجيل الخروج'
        }, status=status.HTTP_400_BAD_REQUEST)
