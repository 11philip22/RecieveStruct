import struct

from fastapi import FastAPI, File
import uvicorn
import construct

test_struct = construct.Struct(
    'dwOemId' / construct.Int32un,
    'wProcessorArchitecture' / construct.Int16un,
    'bIsWindowsServer' / construct.Int,
    'cUsername' / construct.Array(257, construct.Int8sn)
)

api = FastAPI()


@api.post("/signing/")
async def create_file(data: bytes = File(...)):
    data = test_struct.parse(data)
    print()
    return {"file_size": len(data)}


@api.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:api", host="127.0.0.1", port=6000, log_level="info")
