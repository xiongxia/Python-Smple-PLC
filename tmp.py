from pymodbus.client.sync import ModbusSerialClient as ModbusClient

import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

UNIT = 0x1


def run_sync_client():

    client = ModbusClient(method='rtu', port='com7', baudrate=9600, timeout=1)  # 客户机(通信方式，端口，波特率，超时)
    client.connect()

    log.debug("读保持寄存器，返回成功与否")
    rr = client.read_holding_registers(1, 1, unit=UNIT)  # 03H读保持寄存器(起始寄存器号，数量，从机号)->返回成功与否
    print(rr)
    client.close()

    log.debug("写保持寄存器并读回")
    rq = client.write_register(0, 333, unit=UNIT)  # 06H写保持寄存器(起始寄存器号，值，从机号)->返回写的数值
    print(rq)  # 写入的数值
    print(rq.function_code)  # 功能码
    rr = client.read_holding_registers(0, 8, unit=UNIT)  # 03H读保持寄存器(起始寄存器号，数量，从机号)->返回成功与否
    print(rr)
    print(rr.registers)  # 读出的数据列表
    assert (rq.function_code < 0x80)  # test that we are not an error
    assert (rr.registers[1] == 666)  # test the expected value


if __name__ == "__main__":
    run_sync_client()
