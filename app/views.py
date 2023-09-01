from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Product
from app.serializer import ProductModelSerializer


@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    if products:
        serializer = ProductModelSerializer(instance=products, many=True)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)
    return Response(data=({"message": "Product is not found"}),
                    status = status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def add_product(request):
    serializer = ProductModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data,
                        status=status.HTTP_201_CREATED)
    return Response(data=serializer.data,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_product(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if product:
        product.delete()
        return Response(data=({"message": "Product is deleted"}),
                        status=status.HTTP_204_NO_CONTENT)
    return Response(data=({"message": "Product not found"}),
                    status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def product(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if product:
        serializer = ProductModelSerializer(instance=product)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)
    return Response(data=({"message": "Product not found"}),
                    status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def update_product(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if not product:
        return Response(data=({"message": "Product not Found"}),
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ProductModelSerializer(instance=product,
                                        data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)
    return Response(data=serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
