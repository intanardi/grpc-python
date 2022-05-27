from concurrent import futures
import time
import timeit
from datetime import datetime, timedelta
import grpc
import grpcapi_pb2_grpc
import grpcapi_pb2
from google.protobuf.timestamp_pb2 import Timestamp
from app.models import User

class GrpcapiServicer(grpcapi_pb2_grpc.GrpcapiServicer):
    def Login(self, request, context):
        print("login Request! ")
        date_log = datetime.now()
        start_time = datetime.now()
        check = User().login(request.username, request.password)
        status = "Login Failed username or password is wrong"
        if check:
            status = "Login Success"
        response = grpcapi_pb2.LoginResponse()
        end_time = datetime.now()
        interval = end_time - start_time
        print_response = '{} : Login process done in {} seconds\n'.format(date_log, interval)
        print(print_response)
        f = open("grpc_speed_log.txt", "a")
        f.write(print_response)
        f.close()
        return response
    
    def GetAllOrder(self, request, context):
        print("Get All Order Request! ")
        date_log = datetime.now()
        start_time = datetime.now()
        response = grpcapi_pb2.GetAllOrderResponse()
        response.total_revenue = 40000
        response.transaction_date.GetCurrentTime()
        response.order.order_no = "abc123"
        response.order.total_items = 2
        response.order.detail.product_id = 1
        response.order.detail.name = "Nasi Goreng"
        response.order.detail.price = 20000
        end_time = datetime.now()
        interval = end_time - start_time
        print_response = '{} : Get All Order process done in {} seconds\n'.format(date_log, interval)
        print(print_response)
        f = open("grpc_speed_log.txt", "a")
        f.write(print_response)
        f.close()
        return response
    
    def GetProductOrder(self, request, context):
        print("get Product Order Request! ")
        date_log = datetime.now()
        start_time = datetime.now()
        timestamp = Timestamp()
        timestamp.GetCurrentTime()
        response = grpcapi_pb2.GetProductOrderResponse()
        response.order_no = "abc123"
        response.id_product = 1
        response.name = "Nasi Goreng"
        response.price = 20000
        response.total_order = 1
        response.total_price = 20000
        response.total = 20000
        end_time = datetime.now()
        interval = end_time - start_time
        print_response = '{} : Get Product Order process done in {} seconds\n'.format(date_log, interval)
        print(print_response)
        f = open("grpc_speed_log.txt", "a")
        f.write(print_response)
        f.close()
        return response



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpcapi_pb2_grpc.add_GrpcapiServicer_to_server(GrpcapiServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


serve()