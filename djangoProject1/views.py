from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
import textract
import djangoProject1.analisys as anal
from djangoProject1.four_serializer import FourSerializer, UploadSerializer


@api_view(['GET', 'POST'])
def test_num(request):
    """
    Get test num
    """
    if request.method == 'GET':
        number = anal.NumsTest(42)
        ser = FourSerializer(number)
        return Response(ser.data)
    elif request.method == 'POST':
        print("FUCK")


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        print(content_type)
        with open("./temp/temp.docx", 'wb+') as dest:
            for chunk in file_uploaded.chunks():
                dest.write(chunk)
        text = textract.process("./temp/temp.docx")
        return Response(text)
