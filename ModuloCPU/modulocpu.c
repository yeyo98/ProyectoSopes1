#include <linux/module.h>
#include <linux/init.h>
#include <linux/proc_fs.h>
#include <linux/sched.h>
#include <linux/uaccess.h>
#include <linux/fs.h>
#include <linux/sysinfo.h>
#include <linux/seq_file.h>
#include <linux/slab.h>
#include <linux/mm.h>
#include <linux/swap.h>
#include <linux/timekeeping.h>

#include <linux/mmzone.h>
#include <linux/blkdev.h>
#include <linux/list.h>
#include <linux/cpumask.h>
#include <linux/kernel_stat.h>

static int my_proc_show(struct seq_file *m, void *v){
	//seq_print(m, "Hola Mundo :)\n");
    unsigned long cpu_bit = *((unsigned long *)cpu_possible_mask->bits);
	unsigned long idx = cpu_bit;

    unsigned long total = 0; // VARIABLE PARA GUARDAR USO TOTAL
    unsigned long idle = 0; // VARIABLE PARA GUARDAR USO IGNORADO
    unsigned long usage = 0; // USADO


    int contador = 0;
	while(idx)
	{
        struct kernel_cpustat *base = 
        (struct kernel_cpustat *)((unsigned long)__per_cpu_offset[contador]+(unsigned long)&kernel_cpustat);
		total   += base->cpustat[CPUTIME_USER];
		total   += base->cpustat[CPUTIME_NICE];
		total    += base->cpustat[CPUTIME_SYSTEM];
        total   += base->cpustat[CPUTIME_IDLE];
		total += base->cpustat[CPUTIME_IOWAIT];

		idle   += base->cpustat[CPUTIME_IDLE];
		idle += base->cpustat[CPUTIME_IOWAIT];

		total   += base->cpustat[CPUTIME_IRQ];
		total   += base->cpustat[CPUTIME_SOFTIRQ];
		total  += base->cpustat[CPUTIME_STEAL];

		contador++;
		idx = idx >> 1;
		// probably convert with cputime64_to_clock_t
	}

    usage = total - idle;
    
	// USAGE, TOTAL
    seq_printf(m, "%lu,%lu",usage,total);

	return 0;
}

static ssize_t my_proc_write(struct file *file, const char __user *buffer, size_t count, loff_t *f_pos){
	return 0;
}

static int my_proc_open(struct inode *inode, struct file *file){
	return single_open(file, my_proc_show, NULL);
}

static struct file_operations my_fops={
	.owner = THIS_MODULE,
	.open = my_proc_open,
	.release = single_release,
	.read = seq_read,
	.llseek = seq_lseek,
	.write = my_proc_write
};

static int __init test_init(void){
	struct proc_dir_entry *entry;
	entry = proc_create("cpu-module", 0777, NULL, &my_fops);
	if(!entry){
		return -1;
	}else{
		printk(KERN_INFO "Inicio\n");
	}
	return 0;
}

static void __exit text_exit(void){
	remove_proc_entry("cpu-module", NULL);
	printk(KERN_INFO "Final\n");
}

module_init(test_init);
module_exit(text_exit);
MODULE_LICENSE("GPL");

