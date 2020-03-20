/**
 * 
 */
package windows;

import java.awt.BorderLayout;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JToolBar;
import javax.swing.border.BevelBorder;

import data.BaseDao;

/**
 * @author 牛冠群
 * @version 1.0
 * @date2019年5月23日下午4:17:24
 * @copyright 小群子怎么那么淑女呢
 * @aim  图书管理系统 主界面
 */
public class MainFrame extends PublicJFrame{
	
	private JMenuItem mi_user_upkeep;  //用户维护 菜单项
	private JMenuItem mi_reader_upkeep;  //读者维护菜单项
	private JMenuItem mi_book_upkeep;   //图书维护
	private JMenuItem mi_borrow;  //借书
	private JMenuItem mi_back;   //还书
	private JMenuItem mi_reader_query;    //读者查询
	private JMenuItem mi_book_query;   //图书查询
	private JMenuItem mi_update_pass;    //修改密码
	private JMenuItem mi_exit;  //退出
	private JMenuItem mi_book_statistics; //图书统计
	
	private JButton bt_reader_upkeep;   //读者维护
	private JButton bt_book_upkeep;    //图书维护
	private JButton bt_borrow;  //借书
	private JButton bt_back;
	private JButton bt_reader_query;
	private JButton bt_book_query;
	private JButton bt_book_statistics;
	private JButton bt_exit;
	
	/**
	 * 系统主界面初始化方法
	 */
	public MainFrame() {
		
		this.setTitle("BMW-LAB图书管理系统_BY小群子");
		this.setExtendedState(JFrame.MAXIMIZED_BOTH);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setJMenuBar(createMenuBar());
		this.add(createToolBar(),BorderLayout.NORTH);
	}
	
	
	private JMenuBar createMenuBar() {
		JMenuBar menuBar = new JMenuBar();
		JMenu menu_upkeep = new JMenu("基础维护");
		mi_user_upkeep = new JMenuItem("用户维护");
		mi_user_upkeep.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent arg0) {
				// TODO Auto-generated method stub
				user_upkeep_actionPerformed();
			}
		});
		
		menu_upkeep.add(mi_user_upkeep);
		
		mi_reader_upkeep = new JMenuItem("读者维护");
		mi_reader_upkeep.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				reader_upkeep_actionPerformed();
			}
		});
		
		menu_upkeep.add(mi_reader_upkeep);
		mi_book_upkeep = new JMenuItem("图书维护");
		mi_book_upkeep.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				book_upkeep_actionPerformed();
			}
		});
		
		menu_upkeep.add(mi_book_upkeep);
		menuBar.add(menu_upkeep);
		JMenu menu_borrow = new JMenu("借阅管理");
		mi_borrow = new JMenuItem("借书");
		mi_borrow.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				borrow_actionPerformed();
			}
		});
		
		menu_borrow.add(mi_borrow);
		
		mi_back = new JMenuItem("还书");
		mi_back.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				back_actionPerformed();
			}
		});
		
		menu_borrow.add(mi_back);
		menuBar.add(menu_borrow);
		JMenu menu_query = new JMenu("查询统计");
		mi_reader_query = new JMenuItem("读者查询");
		mi_reader_query.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				reader_query_actionPerformed();
			}
		});
		menu_query.add(mi_reader_query);
		
		mi_book_query = new JMenuItem("图书查询");
		mi_book_query.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				book_query_actionPerformed();
			}
		});
		menu_query.add(mi_book_query);
		
		
		mi_book_statistics = new JMenuItem("图书统计");
		mi_book_statistics.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				book_statistics_actionPerformed();
			}
		});
		menu_query.add(mi_book_statistics);
		menuBar.add(menu_query);
		
		JMenu menu_management = new JMenu("系统管理");
		mi_update_pass = new JMenuItem("修改密码");
		mi_update_pass.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				update_pass_actionPerformed();
			}
		});
		menu_management.add(mi_update_pass);
		
		mi_exit = new JMenuItem("退出系统");
		mi_exit.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				exit_actionPerformed();
			}
		});
		menu_management.add(mi_exit);
		menuBar.add(menu_management);
		return menuBar;	
	}
	
	/**
	 * 创建工具栏方法
	 * @return
	 */
	private JToolBar createToolBar() {
		JToolBar toolBar = new JToolBar("图书管理系统工具栏");
		toolBar.setFloatable(false);   //设置工具栏不可浮动
		toolBar.setBorder(new BevelBorder(BevelBorder.LOWERED));
		bt_reader_upkeep = new JButton("读者维护");
		ImageIcon icon_reader_upkeep = new ImageIcon("images/reader_upkeep.png");
		icon_reader_upkeep.setImage(icon_reader_upkeep.getImage().getScaledInstance(100, 100, 100));
		bt_reader_upkeep.setIcon(icon_reader_upkeep);
		bt_reader_upkeep.setToolTipText("读者维护");
		bt_reader_upkeep.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent arg0) {
				// TODO Auto-generated method stub
				reader_upkeep_actionPerformed();
			}
		});
		toolBar.add(bt_reader_upkeep);
		
		bt_book_upkeep = new JButton("图书维护");
		ImageIcon icon_book_upkeep = new ImageIcon("images/book_upkeep.png");
		icon_book_upkeep.setImage(icon_book_upkeep.getImage().getScaledInstance(100, 100, 100));
		bt_book_upkeep.setIcon(icon_book_upkeep);
		toolBar.add(bt_book_upkeep);
		bt_book_upkeep.addActionListener(new ActionListener() {
		
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				book_upkeep_actionPerformed();
			}
		});
		
		bt_borrow = new JButton("借书");
		ImageIcon icon_borrow = new ImageIcon("images/borrow.png");
		icon_borrow.setImage(icon_borrow.getImage().getScaledInstance(100, 100, 100));
		bt_borrow.setIcon(icon_borrow);
		toolBar.add(bt_borrow);
		bt_borrow.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				borrow_actionPerformed();
			}
		});
		
		bt_back = new JButton("还书");
		ImageIcon icon_back = new ImageIcon("images/back.png");
		icon_back.setImage(icon_back.getImage().getScaledInstance(100, 100, 100));
		bt_back.setIcon(icon_back);
		toolBar.add(bt_back);
		bt_back.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				back_actionPerformed();
			}
		});
		
		bt_reader_query = new JButton("读者查询");
		ImageIcon icon_reader_query = new ImageIcon("images/reader_query.png");
		icon_reader_query.setImage(icon_reader_query.getImage().getScaledInstance(100, 100, 25));
		bt_reader_query.setIcon(icon_reader_query);
		toolBar.add(bt_reader_query);
		bt_reader_query.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				reader_query_actionPerformed();
			}
		});
		
		bt_book_query = new JButton("图书查询");
		ImageIcon icon_book_query = new ImageIcon("images/book_query.png");
		icon_book_query.setImage(icon_book_query.getImage().getScaledInstance(100, 100, 25));
		bt_book_query.setIcon(icon_book_query);
		toolBar.add(bt_book_query);
		bt_book_query.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				book_query_actionPerformed();
			}
		});
		
		bt_book_statistics = new JButton("图书统计");
		ImageIcon icon_book_statistics = new ImageIcon("images/book_statistics.png");
		icon_book_statistics.setImage(icon_book_statistics.getImage().getScaledInstance(100, 100, 25));
		bt_book_statistics.setIcon(icon_book_statistics);
		toolBar.add(bt_book_statistics);
		bt_book_statistics.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				book_statistics_actionPerformed();
			}
		});
		
		bt_exit = new JButton("退出系统");
		ImageIcon icon_exit = new ImageIcon("images/exit.png");
		icon_exit.setImage(icon_exit.getImage().getScaledInstance(100, 100, 25));
		bt_exit.setIcon(icon_exit);
		toolBar.add(bt_exit);
		bt_exit.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				exit_actionPerformed();
			}
		});
		
		return toolBar;
	}
	
	/**
	 * 设置系统功能使用权限的方法
	 * @param purView
	 */
	void setPurView(byte purView) {
		switch (purView) {
		case 0://操作员
			mi_user_upkeep.setEnabled(false);//用户维护不可用
			mi_book_statistics.setEnabled(false);
			bt_book_statistics.setEnabled(false);
			break;
		case 1:
			break;

		default:
			mi_user_upkeep.setEnabled(false);
			mi_reader_upkeep.setEnabled(false);
			mi_book_upkeep.setEnabled(false);
			mi_borrow.setEnabled(false);
			mi_back.setEnabled(false);
			mi_book_statistics.setEnabled(false);
			mi_update_pass.setEnabled(false);
			
			bt_book_statistics.setEnabled(false);
			bt_reader_upkeep.setEnabled(false);
			bt_book_upkeep.setEnabled(false);
			bt_borrow.setEnabled(false);
			bt_back.setEnabled(false);
		}
	}
	
	/**
	 * 用户维护响应方法
	 */
	private void user_upkeep_actionPerformed() {
		new UserUpkeep();
	}
	
	/**
	 * 读者维护响应方法
	 */
	private void reader_upkeep_actionPerformed() {
		new ReaderUpkeep();
	}
	
	/**
	 * 图书维护方法
	 */
	private void book_upkeep_actionPerformed() {
		new BookUpkeep();
	}
	
	/**
	 * 借书响应
	 */
	private void borrow_actionPerformed() {
		//new Borrow();
	}
	
	private void back_actionPerformed() {
		//new back();
	}

	private void reader_query_actionPerformed() {
		new ReaderQuery();
	}
	
	private void book_query_actionPerformed() {
		new BookQuery();
	}
	
	private void book_statistics_actionPerformed() {
		//new BookStatistics();
	}
	
	private void update_pass_actionPerformed() {
		new UpdatePass();
	}
	
	private void exit_actionPerformed() {
		BaseDao.close();
		System.exit(0);
	}
	
	//public static void main(String args[]) {
	//	new MainFrame();
	//}
	
}
