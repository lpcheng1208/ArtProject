import multiprocessing
import time


def work(msg):
    mult_proces_name = multiprocessing.current_process().name
    print('process: ' + mult_proces_name + '-' + msg)


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=5)  # 创建4个进程
    for i in range(20):
        msg = "process %d" % (i)
        pool.apply_async(work, (msg,))
    pool.close()  # 关闭进程池，表示不能在往进程池中添加进程
    pool.join()  # 等待进程池中的所有进程执行完毕，必须在close()之后调用
    print("Sub-process all done.")