import "./EventCard.css";

interface Props{
    children:React.ReactNode;
}

export default function EventCard({children}:Props){

    return(

        <div className="event-card">

            <h3>Eventos Recentes</h3>

            <div className="event-content">

                {children}

            </div>

        </div>

    );

}