import grpcapi_pb2_grpc
import grpcapi_pb2
import time
import datetime
import grpc
import logging

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpcapi_pb2_grpc.GrpcapiStub(channel)
        logger = logging.getLogger()
        handler = logging.FileHandler('logfile.log')
        logger.addHandler(handler)
        print_response = "Service call failed"
        print("which service you want to call? 1 = login; 2 = Get All Order; 3 = Get Product Order")
        rpc_service = int(input())
        print("---")
        if rpc_service == 1:
            timestamp = datetime.datetime.now()
            start = time.time()
            login_req = grpcapi_pb2.LoginRequest(username = "ardi", password = "12345")
            login_response = stub.Login(login_req)
            print(login_response)
            end = time.time()
            duration = end - start
            print_response = '{} : login process done in {} seconds'.format(timestamp, duration)
        elif rpc_service == 2:
            timestamp = datetime.datetime.now()
            start = time.time()
            getAllOrder_request = grpcapi_pb2.GetAllOrderRequest()
            getAllOrder_response = stub.GetAllOrder(getAllOrder_request)
            print(getAllOrder_response)
            end = time.time()
            duration = end - start
            print_response = '{} : Get All Order process done in {} seconds'.format(timestamp, duration)
        elif rpc_service == 3:
            timestamp = datetime.datetime.now()
            start = time.time()
            getProduct_request = grpcapi_pb2.GetProductOrderRequest(order_no = "abc123")
            getProduct_response = stub.GetProductOrder(getProduct_request)
            print(getProduct_response)
            end = time.time()
            duration = end - start
            print_response = '{} : Get Product Order process done in {} seconds'.format(timestamp, duration)
        
        # logger.error(print_response)
        print("done")


if __name__ == "__main__":
    run()