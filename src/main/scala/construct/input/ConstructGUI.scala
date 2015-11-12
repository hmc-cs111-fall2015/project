package construct.input

import scala.tools.nsc.EvalLoop
import java.awt.image.BufferedImage
import scala.swing._
import construct.input.parser.ConstructParser
import construct.semantics.ConstructInterpreter
import construct.output.PNG

object ConstructGUI extends EvalLoop with App {
  override def prompt = "Statement> "
  val ui = new UI
  ui.visible = true

  var interpreter = new ConstructInterpreter
  var first = true
  loop { line =>
    if (first) {
      first = false
      ConstructParser.parseGivens(line) match {
        case ConstructParser.Success(t, _) => {
          interpreter.inputs(t, None)
        }
        case e: ConstructParser.NoSuccess  => println(e)
      }
    }
    else if (line == ":reset" || line == ":r") {
      interpreter = new ConstructInterpreter
      first = true
    }
    else if (line == ":draw" || line == ":d") {
      PNG.dump(interpreter.objects)
    }
    else {
      ConstructParser.parseStatement(line) match {
        case ConstructParser.Success(t, _) => {
          interpreter.execute(t)
        }
        case e: ConstructParser.NoSuccess  => println(e)
      }
    }
    ui.setImage(PNG.get(interpreter.objects))
  }
  ui.dispose()
}


class ImagePanel extends Panel
{
  private var _bufferedImage: BufferedImage = null

  def setImage(value: BufferedImage) =
  {
    _bufferedImage = value
  }

  override def paintComponent(g:Graphics2D) =
  {
    if (null != _bufferedImage) g.drawImage(_bufferedImage, 0, 0, null)
  }
}

class UI extends MainFrame {
  title = "Construct"
  preferredSize = new Dimension(500, 500)
  private val image = new ImagePanel()
  contents = image
  def setImage(img: BufferedImage) = {
    image.setImage(img)
    repaint()
  }
}
