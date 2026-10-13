from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .srialayzer import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class ProductOnlyListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductOnlyCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(f"Vnimanie! Polzovatel {self.request.user.username} sozdaet novyy produkt.")
        serializer.save(created_by=self.request.user)

class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_quesryset(self):
        user = self.request.user
        return Product.objects.filter(created_by=user)


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDestroyView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    