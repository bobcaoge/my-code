/**
 * 
 */
package windows;

import java.awt.Color;
import java.awt.Image;

import javax.swing.JFrame;

/**
 * @author ţ��Ⱥ
 * @version 1.0
 * @date2019��5��23������2:18:36
 * @copyright СȺ����ô��ô��Ů��
 * @aim  ���н���Ļ������ ����ͳһϵͳͼ�� ������ɫ��
 */
public class PublicJFrame extends JFrame{
	
	PublicJFrame(){
		//���������ý����ܵ�ͼ��
		Image icon = new JFrame().getToolkit().getImage("images/icon.png");
		this.setIconImage(icon);
		//���ÿ���������ı�����ɫ
		this.getContentPane().setBackground(new Color(210,242,243));
		this.setVisible(true);   //���ÿ�ܿɼ�
	}

}
