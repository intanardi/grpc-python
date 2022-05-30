FROM python:3.8-slim

COPY myapp_server.py /pygrpc/myapp_server.py
COPY myapp_server.py /pygrpc/myapp_client.py
COPY /protos/grpcapi.proto /pygrpc/protos/grpcapi.proto
COPY grpcapi_pb2_grpc /pygrpc/grpcapi_pb2_grpc.py
COPY grpcapi_pb2 /pygrpc/grpcapi_pb2

CMD ["python", "/pygrpc/myapp_server.py"]