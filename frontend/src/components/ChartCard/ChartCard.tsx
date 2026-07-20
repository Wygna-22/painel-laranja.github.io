import "./ChartCard.css";

interface Props{
    title:string;
    children:React.ReactNode;
}

export default function ChartCard({title, children}:Props){

    return(

        <section className="chart-card">

            <div className="chart-header">

                <h3>{title}</h3>

            </div>

            <div className="chart-content">

                {children}

            </div>

        </section>

    );

}