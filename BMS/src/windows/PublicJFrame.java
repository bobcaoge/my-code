/**
 * 
 */
package windows;

import java.awt.Color;
import java.awt.Image;

import javax.swing.JFrame;

/**
 * @author 牛冠群
 * @version 1.0
 * @date2019年5月23日下午2:18:36
 * @copyright 小群子怎么那么淑女呢
 * @aim  所有界面的基础框架 用来统一系统图标 背景颜色等
 */
public class PublicJFrame extends JFrame{
	
	PublicJFrame(){
		//创建、设置界面框架的图标
		Image icon = new JFrame().getToolkit().getImage("images/icon.png");
		this.setIconImage(icon);
		//设置框架内容面板的背景颜色
		this.getContentPane().setBackground(new Color(210,242,243));
		this.setVisible(true);   //设置框架可见
	}

}
