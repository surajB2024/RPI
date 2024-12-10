#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/export-internal.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

#ifdef CONFIG_UNWINDER_ORC
#include <asm/orc_header.h>
ORC_HEADER;
#endif

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif



static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0xa810cb28, "usb_alloc_urb" },
	{ 0x44b5ab63, "usb_free_urb" },
	{ 0xef0e635e, "param_ops_uint" },
	{ 0xbb85aaa4, "param_ops_ulong" },
	{ 0x7f02188f, "__msecs_to_jiffies" },
	{ 0x5e515be6, "ktime_get_ts64" },
	{ 0x28db3b0f, "usb_get_current_frame_number" },
	{ 0xa6875084, "proc_create" },
	{ 0x44adfee, "param_ops_ushort" },
	{ 0x28fa15f1, "consume_skb" },
	{ 0x5a9f1d63, "memmove" },
	{ 0x656e4a6e, "snprintf" },
	{ 0xacf5be9d, "sysfs_add_file_to_group" },
	{ 0x6a0b3b1a, "alloc_canfd_skb" },
	{ 0x92540fbf, "finish_wait" },
	{ 0x48f600d0, "usb_register_driver" },
	{ 0x16193702, "param_array_ops" },
	{ 0x4829a47e, "memcpy" },
	{ 0x37a0cba, "kfree" },
	{ 0xe67c066d, "seq_lseek" },
	{ 0x8c26d495, "prepare_to_wait_event" },
	{ 0xf6ebc03b, "net_ratelimit" },
	{ 0xe2964344, "__wake_up" },
	{ 0x2fbf7ae5, "param_ops_byte" },
	{ 0x34db050b, "_raw_spin_lock_irqsave" },
	{ 0xb22a98e3, "open_candev" },
	{ 0x7a67c1a, "__dev_get_by_name" },
	{ 0xcc5005fe, "msleep_interruptible" },
	{ 0x20b6a028, "netdev_err" },
	{ 0x122c3a7e, "_printk" },
	{ 0x75bf7df6, "usb_clear_halt" },
	{ 0x8ddd8aad, "schedule_timeout" },
	{ 0x1000e51, "schedule" },
	{ 0x2b1719fa, "usb_bulk_msg" },
	{ 0xaa0f95e9, "usb_reset_device" },
	{ 0xf0fdf6cb, "__stack_chk_fail" },
	{ 0x6cbbfc54, "__arch_copy_to_user" },
	{ 0x9f614b85, "alloc_can_skb" },
	{ 0xce9d6cdf, "unregister_candev" },
	{ 0x5c5781c2, "usb_submit_urb" },
	{ 0x141e757c, "_dev_info" },
	{ 0x524eee6c, "can_change_mtu" },
	{ 0x167c5967, "print_hex_dump" },
	{ 0xfe487975, "init_wait_entry" },
	{ 0x24a6214b, "init_net" },
	{ 0x125696da, "alloc_candev_mqs" },
	{ 0x1e6d26a8, "strstr" },
	{ 0x2af86b37, "kfree_skb_reason" },
	{ 0x4dfa8d4b, "mutex_lock" },
	{ 0x5a921311, "strncmp" },
	{ 0x52e02d0c, "usb_control_msg" },
	{ 0x9166fada, "strncpy" },
	{ 0xd7f54667, "free_netdev" },
	{ 0x5f37eeba, "usb_set_interface" },
	{ 0x1edb69d6, "ktime_get_raw_ts64" },
	{ 0x7002f9fd, "class_unregister" },
	{ 0x9ec6ca96, "ktime_get_real_ts64" },
	{ 0x33a3d159, "sysfs_remove_file_from_group" },
	{ 0xfef216eb, "_raw_spin_trylock" },
	{ 0xbcab6ee6, "sscanf" },
	{ 0xcefb0c9f, "__mutex_init" },
	{ 0x951c6f79, "usb_deregister" },
	{ 0x37befc70, "jiffies_to_msecs" },
	{ 0xd35cce70, "_raw_spin_unlock_irqrestore" },
	{ 0x205bea7c, "netif_tx_wake_queue" },
	{ 0x65929cae, "ns_to_timespec64" },
	{ 0x261615f2, "close_candev" },
	{ 0xdbdf6c92, "ioport_resource" },
	{ 0xdcb764ad, "memset" },
	{ 0x6bea4453, "param_ops_charp" },
	{ 0xd9a5ea54, "__init_waitqueue_head" },
	{ 0x8c8f0578, "netif_rx" },
	{ 0x28832e42, "can_bus_off" },
	{ 0xe2d5255a, "strcmp" },
	{ 0x15ba50a6, "jiffies" },
	{ 0x1f955396, "seq_read" },
	{ 0x3c3ff9fd, "sprintf" },
	{ 0x21d13a58, "device_create_with_groups" },
	{ 0x3213f038, "mutex_unlock" },
	{ 0xc6f46339, "init_timer_key" },
	{ 0xeae3dfd6, "__const_udelay" },
	{ 0xe2097a9d, "driver_for_each_device" },
	{ 0xde81aa90, "__register_chrdev" },
	{ 0xb86bb5ac, "device_destroy" },
	{ 0x49f6cfe3, "remove_proc_entry" },
	{ 0x6b93e122, "usb_kill_urb" },
	{ 0x404ea81a, "seq_printf" },
	{ 0xffeedf6a, "delayed_work_timer_fn" },
	{ 0x20000329, "simple_strtoul" },
	{ 0x12a4e128, "__arch_copy_from_user" },
	{ 0x6f436062, "netif_carrier_on" },
	{ 0xeabb347, "usb_reset_endpoint" },
	{ 0x91ab7f29, "single_release" },
	{ 0xa65c6def, "alt_cb_patch_nops" },
	{ 0x3092a983, "alloc_can_err_skb" },
	{ 0x726340e0, "kmalloc_trace" },
	{ 0x98cf60b3, "strlen" },
	{ 0xc73bf268, "single_open" },
	{ 0x349cba85, "strchr" },
	{ 0x3d542e6c, "register_candev" },
	{ 0xd3e40520, "class_register" },
	{ 0xc4f0da12, "ktime_get_with_offset" },
	{ 0xeb233a45, "__kmalloc" },
	{ 0x9a631eb1, "kmalloc_caches" },
	{ 0xa880f547, "netdev_info" },
	{ 0x85bd1608, "__request_region" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0x67a35d9, "module_layout" },
};

MODULE_INFO(depends, "can-dev");

MODULE_ALIAS("usb:v0C72p000Cd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0C72p000Dd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0C72p0012d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0C72p0011d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0C72p0013d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0C72p0014d*dc*dsc*dp*ic*isc*ip*in*");

MODULE_INFO(srcversion, "B92E12B6035966850D7D94A");
