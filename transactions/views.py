from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Request, Response, status

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)


        positive_sum = sum(float(item["value"]) for item in serializer.data if not item["type"] == "Boleto" or not item["type"] == "Financiamento" or not item["type"] == "Aluguel")

        negative_sum = sum(float(item["value"]) for item in serializer.data if item["type"] == "Boleto" or item["type"] == "Financiamento" or item["type"] == "Aluguel")

        balance = {
            "cash_in": positive_sum,
            "cash_out": negative_sum,
            "final_balance": positive_sum - negative_sum
        }

        return Response({"balance": balance, "transactions": serializer.data})

    def create(self, request: Request):
        file = request.FILES["file"]
        content = file.read().decode("utf-8").split("\n")
        
        response_list = []
        for transaction in content:
            new_dict = self.create_formated_dict(transaction)
            serializer = self.get_serializer(data=new_dict)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_list.append(serializer.data)
        
        return Response(response_list, status=status.HTTP_201_CREATED)

    def create_formated_dict(self, line):
        type = self.type_format(line[0:1])
        date = line[1:9]
        value = float(line[9:19])/100
        cpf = line[19:30]
        card = line[30:42]
        time = line[42:48]
        shop_owner = line[48:62].strip()
        shop = line[62:81].strip()

        date = date[:4] + "-" + date[4:6] + "-" + date[6:]
        time = time[:2] + ":" + time[2:4] + ":" + time[4:]

        new_dict = {
            "type": type,
            "date": date,
            "value": value,
            "cpf": cpf,
            "card": card,
            "time": time,
            "shop_owner": shop_owner,
            "shop": shop,
        }

        return new_dict
        
    def type_format(self, type):
        match type:
            case "1":
                return "D??bito"
            case "2":
                return "Boleto"
            case "3":
                return "Financiamento"
            case "4":
                return "Cr??dito"
            case "5":
                return "Recebimento Empr??stimo"
            case "6":
                return "Vendas"
            case "7":
                return "Recebimento TED"
            case "8":
                return "Recebimento DOC"
            case "9":
                return "Aluguel"


class TransactionRetrieveView(RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "transaction_id"

