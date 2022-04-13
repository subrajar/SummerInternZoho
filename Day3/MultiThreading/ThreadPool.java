package multithreading;

import java.util.concurrent.*;

public class ThreadPool {
	public static void main(String[] arges) {
		int coreCount=Runtime.getRuntime().availableProcessors();
		System.out.println(coreCount);
		ExecutorService service=Executors.newFixedThreadPool(5);
		for(int i=0;i<50;i++) {
			service.execute(new Task());
		}
	}

}
class Task implements Runnable{
	public void run() {
		System.out.println(Thread.currentThread().getName());
	}
}
