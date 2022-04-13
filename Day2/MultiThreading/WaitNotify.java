package multithreading;

class Customer {
	int amount = 10000;

	public synchronized void withdraw(int amount) {
		System.out.println("going to withdraw amount");

		if (this.amount < amount) {
			System.out.println("Less balance");
			try {
				wait();
			} catch (Exception e) {
			}
		}
		this.amount -= amount;
		if(amount==15000)
			System.out.println("withdraw1 completed");
		else
			System.out.println("withdraw2 compleated");
	}

	synchronized void deposit(int amount) {
		System.out.println("going to deposit amount");
		this.amount += amount;
		System.out.println("deposit completed");
		notify();
	}
}

public class WaitNotify {
	public static void main(String args[]) {
		Customer c = new Customer();
		new Thread() {
			public void run() {
				c.withdraw(12000);
			}
		}.start();
		new Thread() {
			public void run() {
				c.withdraw(15000);
			}
		}.start();
		
		new Thread() {
			public void run() {
				c.deposit(10000);
			}
		}.start();

	}
}
