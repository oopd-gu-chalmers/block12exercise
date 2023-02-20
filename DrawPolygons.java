/* Model- ... */
import edu.chalmers_gu_cse.oopd.exercises.polygonModel.PolygonModel;
import edu.chalmers_gu_cse.oopd.exercises.polygonModel.shapes.*;
/* -View- ... */
import edu.chalmers_gu_cse.oopd.exercises.view2d.PolygonViewer;
/* -Controller */
import edu.chalmers_gu_cse.oopd.exercises.controller.PolygonClicker;

public class DrawPolygons {

    public static void main(String[] args) {
        /* Create a new model. */
        PolygonModel polygons = createModel();
        /* Create a view that listens to the model and can display it. */
        PolygonViewer view = createViewForModel(polygons);
        /* Create a controller that sends signals to the model to create
           and add new polygons.
         */
        PolygonClicker controller = new PolygonClicker(polygons);
        /* Make sure that the controller listens to the correct event
           in the UI.
         */
        controller.initInteraction(view);

        polygons.animate();

    }//main

    public static PolygonModel createModel(){
        PolygonModel polygons = new PolygonModel();

        polygons.addPolygon(PolygonFactory.createSquare(50,50));
        polygons.addPolygon(PolygonFactory.createTriangle(100,100));
        polygons.addPolygon(PolygonFactory.createRectangle(50,150));

        return polygons;
    }//initModel

    private static PolygonViewer createViewForModel(PolygonModel polygonModel) {
        PolygonViewer view = new PolygonViewer();
        view.addModel(polygonModel);
        polygonModel.addListener(view);
        return view;
    }//initViewForModel

}//DrawPolygons