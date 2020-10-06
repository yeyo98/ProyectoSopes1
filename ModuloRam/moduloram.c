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


#include <linux/kernel.h>
#include <linux/hugetlb.h>
#include <linux/mman.h>
#include <linux/mmzone.h>
#include <linux/percpu.h>
#include <linux/vmstat.h>
#include <linux/atomic.h>
#include <linux/vmalloc.h>
#ifdef CONFIG_CMA
#include <linux/cma.h>
#endif
#include <asm/page.h>
#include <asm/pgtable.h>

extern unsigned long total_swapcache_pages(void);
#define total_swapcache_pages()			0UL

static int my_proc_show(struct seq_file *m, void *v){
	//seq_print(m, "Hola Mundo :)\n");
    struct sysinfo i;
    unsigned long totalRam, free, buffer, total;
	long cached;

    si_meminfo(&i);
    cached = global_node_page_state(NR_FILE_PAGES) -
			total_swapcache_pages() - i.bufferram;
            
    if (cached < 0)
		cached = 0;

    //disponible = si_mem_available() << (PAGE_SHIFT - 10);
    totalRam = i.totalram << (PAGE_SHIFT - 10);
    free = i.freeram << (PAGE_SHIFT - 10);
    cached = cached << (PAGE_SHIFT - 10);
    buffer = i.bufferram << (PAGE_SHIFT - 10);
    // CALCULO DE LA MEMORIA USADA
    total = free + buffer + cached 
	total = totalRam - total
    total = (total/totalRam) * 100;
    seq_printf(m, "<h1>Total Ram: %lu, Libre: %lu, Cached:%ld, Buffer:%lu, Total:%lu </h1>\n",
                        totalRam,free,cached,buffer,total);

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
	entry = proc_create("ram-module", 0777, NULL, &my_fops);
	if(!entry){
		return -1;
	}else{
		printk(KERN_INFO "Inicio\n");
	}
	return 0;
}

static void __exit text_exit(void){
	remove_proc_entry("ram-module", NULL);
	printk(KERN_INFO "Final\n");
}

module_init(test_init);
module_exit(text_exit);
MODULE_LICENSE("GPL");

