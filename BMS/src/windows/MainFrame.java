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
 * @author ţ��Ⱥ
 * @version 1.0
 * @date2019��5��23������4:17:24
 * @copyright СȺ����ô��ô��Ů��
 * @aim  ͼ�����ϵͳ ������
 */
public class MainFrame extends PublicJFrame{
	
	private JMenuItem mi_user_upkeep;  //�û�ά�� �˵���
	private JMenuItem mi_reader_upkeep;  //����ά���˵���
	private JMenuItem mi_book_upkeep;   //ͼ��ά��
	private JMenuItem mi_borrow;  //����
	private JMenuItem mi_back;   //����
	private JMenuItem mi_reader_query;    //���߲�ѯ
	private JMenuItem mi_book_query;   //ͼ���ѯ
	private JMenuItem mi_update_pass;    //�޸�����
	private JMenuItem mi_exit;  //�˳�
	private JMenuItem mi_book_statistics; //ͼ��ͳ��
	
	private JButton bt_reader_upkeep;   //����ά��
	private JButton bt_book_upkeep;    //ͼ��ά��
	private JButton bt_borrow;  //����
	private JButton bt_back;
	private JButton bt_reader_query;
	private JButton bt_book_query;
	private JButton bt_book_statistics;
	private JButton bt_exit;
	
	/**
	 * ϵͳ�������ʼ������
	 */
	public MainFrame() {
		
		this.setTitle("BMW-LABͼ�����ϵͳ_BYСȺ��");
		this.setExtendedState(JFrame.MAXIMIZED_BOTH);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setJMenuBar(createMenuBar());
		this.add(createToolBar(),BorderLayout.NORTH);
	}
	
	
	private JMenuBar createMenuBar() {
		JMenuBar menuBar = new JMenuBar();
		JMenu menu_upkeep = new JMenu("����ά��");
		mi_user_upkeep = new JMenuItem("�û�ά��");
		mi_user_upkeep.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent arg0) {
				// TODO Auto-generated method stub
				user_upkeep_actionPerformed();
			}
		});
		
		menu_upkeep.add(mi_user_upkeep);
		
		mi_reader_upkeep = new JMenuItem("����ά��");
		mi_reader_upkeep.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				reader_upkeep_actionPerformed();
			}
		});
		
		menu_upkeep.add(mi_reader_upkeep);
		mi_book_upkeep = new JMenuItem("ͼ��ά��");
		mi_book_upkeep.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				book_upkeep_actionPerformed();
			}
		});
		
		menu_upkeep.add(mi_book_upkeep);
		menuBar.add(menu_upkeep);
		JMenu menu_borrow = new JMenu("���Ĺ���");
		mi_borrow = new JMenuItem("����");
		mi_borrow.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				borrow_actionPerformed();
			}
		});
		
		menu_borrow.add(mi_borrow);
		
		mi_back = new JMenuItem("����");
		mi_back.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				back_actionPerformed();
			}
		});
		
		menu_borrow.add(mi_back);
		menuBar.add(menu_borrow);
		JMenu menu_query = new JMenu("��ѯͳ��");
		mi_reader_query = new JMenuItem("���߲�ѯ");
		mi_reader_query.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				reader_query_actionPerformed();
			}
		});
		menu_query.add(mi_reader_query);
		
		mi_book_query = new JMenuItem("ͼ���ѯ");
		mi_book_query.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				book_query_actionPerformed();
			}
		});
		menu_query.add(mi_book_query);
		
		
		mi_book_statistics = new JMenuItem("ͼ��ͳ��");
		mi_book_statistics.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				book_statistics_actionPerformed();
			}
		});
		menu_query.add(mi_book_statistics);
		menuBar.add(menu_query);
		
		JMenu menu_management = new JMenu("ϵͳ����");
		mi_update_pass = new JMenuItem("�޸�����");
		mi_update_pass.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				update_pass_actionPerformed();
			}
		});
		menu_management.add(mi_update_pass);
		
		mi_exit = new JMenuItem("�˳�ϵͳ");
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
	 * ��������������
	 * @return
	 */
	private JToolBar createToolBar() {
		JToolBar toolBar = new JToolBar("ͼ�����ϵͳ������");
		toolBar.setFloatable(false);   //���ù��������ɸ���
		toolBar.setBorder(new BevelBorder(BevelBorder.LOWERED));
		bt_reader_upkeep = new JButton("����ά��");
		ImageIcon icon_reader_upkeep = new ImageIcon("images/reader_upkeep.png");
		icon_reader_upkeep.setImage(icon_reader_upkeep.getImage().getScaledInstance(100, 100, 100));
		bt_reader_upkeep.setIcon(icon_reader_upkeep);
		bt_reader_upkeep.setToolTipText("����ά��");
		bt_reader_upkeep.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent arg0) {
				// TODO Auto-generated method stub
				reader_upkeep_actionPerformed();
			}
		});
		toolBar.add(bt_reader_upkeep);
		
		bt_book_upkeep = new JButton("ͼ��ά��");
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
		
		bt_borrow = new JButton("����");
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
		
		bt_back = new JButton("����");
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
		
		bt_reader_query = new JButton("���߲�ѯ");
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
		
		bt_book_query = new JButton("ͼ���ѯ");
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
		
		bt_book_statistics = new JButton("ͼ��ͳ��");
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
		
		bt_exit = new JButton("�˳�ϵͳ");
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
	 * ����ϵͳ����ʹ��Ȩ�޵ķ���
	 * @param purView
	 */
	void setPurView(byte purView) {
		switch (purView) {
		case 0://����Ա
			mi_user_upkeep.setEnabled(false);//�û�ά��������
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
	 * �û�ά����Ӧ����
	 */
	private void user_upkeep_actionPerformed() {
		new UserUpkeep();
	}
	
	/**
	 * ����ά����Ӧ����
	 */
	private void reader_upkeep_actionPerformed() {
		new ReaderUpkeep();
	}
	
	/**
	 * ͼ��ά������
	 */
	private void book_upkeep_actionPerformed() {
		new BookUpkeep();
	}
	
	/**
	 * ������Ӧ
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
